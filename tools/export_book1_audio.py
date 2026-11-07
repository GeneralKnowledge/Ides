#!/usr/bin/env python3
"""Free audiobook of Book 1: one MP3 per chapter plus an M4B with chapter markers.

Uses Kokoro-82M (Apache-2.0), an open text-to-speech model that runs offline on
the CPU, so there is no account, key, or per-character charge. The reading text
is the same as the docx/EPUB reading copy (export_book1_docx.reading_paragraphs):
the prologue, five act announcements, 38 chapters and the historical note. The
cast list, offices page and timeline are left out of the audio; they are
reference pages for the eye.

Latin and Greek names go through LEXICON below (traditional English
pronunciation, British phonemes) because the stock phonemiser gets some of them
wrong (Cicero as "Sigh-sro", Ides as "eye-DEEZ").

Setup (once):
    pip install kokoro-onnx soundfile
    # ffmpeg must be on PATH
    python3 tools/export_book1_audio.py --fetch-model

Usage:
    python3 tools/export_book1_audio.py --list                 # tracks, word counts
    python3 tools/export_book1_audio.py --samples              # short clip per voice
    python3 tools/export_book1_audio.py --voice bm_george      # everything
    python3 tools/export_book1_audio.py --only 3,4 --voice bm_george
    python3 tools/export_book1_audio.py --m4b-only             # rebuild M4B from WAVs

Output goes to exports/audiobook/ (untracked): wav/ (working files, resumable),
mp3/NN Title.mp3, and Ides_Book1_audiobook.m4b.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_book1_docx as dx  # noqa: E402

OUT = dx.EXPORTS / "audiobook"
MODELS = dx.ROOT / "build" / "kokoro"
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
MODEL_FILES = ("kokoro-v1.0.onnx", "voices-v1.0.bin")
LANG = "en-gb"
RATE = 24000

TITLE = "The Ides of March: Book 1"
AUTHOR = "Reuben Dennison"
BRITISH_VOICES = ("bf_emma", "bm_george", "bm_fable", "bf_isabella", "bm_lewis", "bm_daniel",
                  "bf_alice", "bf_lily")

# Pauses, in seconds.
PARA_GAP = 0.55
SCENE_GAP = 1.6
HEAD_GAP = 1.2
TRACK_TAIL = 2.0

# Traditional English pronunciation of names the phonemiser gets wrong, as British
# IPA in the phonemiser's own notation (stress mark before the stressed vowel).
# A trailing ’s or 's is added automatically.
LEXICON = {
    "Cicero": "sˈɪsəɹəʊ",
    "Laberius": "ləbˈɪəɹɪəs",
    "Ides": "ˈaɪdz",
    "Agrippa": "ɐɡɹˈɪpə",
    "Phileros": "fˈɪləɹɒs",
    "Calenus": "kɐlˈiːnəs",
    "Amyntas": "ɐmˈɪntəs",
    "Kalends": "kˈaləndz",
    "Carinae": "kɐɹˈiːnaɪ",
    "Visellius": "vɪsˈɛlɪəs",
    "Tertulla": "tɜːtˈʊlə",
    "Cleanthes": "kliːˈanθiːz",
    "Faberius": "fɐbˈɪəɹɪəs",
    "Tubero": "tjˈuːbəɹəʊ",
    "Antium": "ˈantɪəm",
    "Domus": "dˈɒməs",
    "Spurinna": "spʊɹˈɪnə",
    "Mutina": "mjˈuːtɪnə",
    "Labeo": "lˈabɪəʊ",
    "Pasiphile": "pɐsˈɪfɪliː",
    "Apollonia": "ˌapəlˈəʊniə",
    "Appian": "ˈapiən",
    "Astura": "astjˈʊəɹə",
    "Argiletum": "ˌɑːɡɪlˈiːtəm",
    "Salernum": "sɐlˈɜːnəm",
    "Reate": "ɹiːˈɑːteɪ",
    "Hadrumetum": "hˌadɹʊmˈiːtəm",
    "Labienus": "lˌabɪˈiːnəs",
    "Albinus": "albˈaɪnəs",
    "Longinus": "lɒndʒˈaɪnəs",
    "Cornutus": "kɔːnjˈuːtəs",
    "Herennius": "həɹˈɛnɪəs",
    "Augustus": "ɔːɡˈʌstəs",
    "Sulpicius": "sʊlpˈɪʃəs",
    "Falernian": "fɐlˈɜːniən",
    "Philologus": "fɪlˈɒləɡəs",
    "Menodotus": "mɛnˈɒdətəs",
    "Apollodorus": "ɐpˌɒlədˈɔːɹəs",
    "Demosthenes": "dɪmˈɒsθəniːz",
    "Volturnus": "vɒltˈɜːnəs",
    "Casilinum": "kˌasɪlˈaɪnəm",
    "Pharsalus": "fɑːsˈeɪləs",
    "Caieta": "kaɪˈiːtə",
    "Puteoli": "pjuːtˈiːəlaɪ",
    "Palatine": "pˈalətaɪn",
    "Gnaeus": "nˈiːəs",
    "Pompeian": "pɒmpˈiːən",
    "Pompeians": "pɒmpˈiːənz",
    "Pompeius": "pɒmpˈeɪəs",
    "Denarius": "dɪnˈeəɹɪəs",
    "denarius": "dɪnˈeəɹɪəs",
    "denarii": "dɪnˈeəɹɪaɪ",
    "Smyrna": "smˈɜːnə",
    "Laodicea": "lˌeɪəʊdɪsˈiːə",
    "Butas": "bjˈuːtəs",
    "Hilarus": "hˈɪləɹəs",
    "Pindarus": "pˈɪndəɹəs",
    "Formiae": "fˈɔːmiː",
    "Andromache": "andɹˈɒməki",
    "Aeneas": "iːnˈiːəs",
    "Aristogeiton": "ɐɹˌɪstədʒˈaɪtən",
    "Agamemnon": "ˌaɡəmˈɛmnɒn",
    "Piraeus": "paɪɹˈiːəs",
    "Acropolis": "ɐkɹˈɒpəlɪs",
    "Eporedia": "ˌɛpəɹˈiːdiə",
    "Capena": "kɐpˈiːnə",
    "Regia": "ɹˈiːdʒiə",
    "Catiline": "kˈatɪlaɪn",
    "Nicolaus": "nˌɪkəlˈeɪəs",
    "Tollere": "tˈɒləɹeɪ",
    "Romanum": "ɹəʊmˈɑːnəm",
    "Ariminum": "ɐɹˈɪmɪnəm",
    "Cularo": "kˈʊləɹəʊ",
    "Ostia": "ˈɒstiə",
    "Octavii": "ɒktˈeɪvɪaɪ",
    "Julii": "dʒˈuːlɪaɪ",
    "Nones": "nˈəʊnz",
    "Lupercal": "lˈuːpəkal",
    "Sphaerus": "sfˈɪəɹəs",
    "Abydos": "ɐbˈaɪdɒs",
    "Thasos": "θˈeɪsɒs",
    "Salamis": "sˈaləmɪs",
    "Philippus": "fɪlˈɪpəs",
    "Sardis": "sˈɑːdɪs",
    "Acilius": "ɐsˈɪlɪəs",
    "Deiotarus": "dˌiːəʊtˈɑːɹəs",
    "Cisalpine": "sɪsˈalpaɪn",
}

_LEX_RE = re.compile(r"\b(" + "|".join(sorted(map(re.escape, LEXICON), key=len, reverse=True))
                     + r")(['’]s)?\b")


# ---------------------------------------------------------------- text ---

def speakable(md: str) -> str:
    """Markdown reading text to plain speech text."""
    t = md.replace("**", "").replace("*", "").replace("†", "").replace("&", "and")
    t = t.replace("•", "").replace("·", "")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def tracks() -> list[dict]:
    """[{n, title, items:[(kind, text)]}] where kind is head|body|scene."""
    _, chapters = dx.load_chapters()
    paras = dx.reading_paragraphs(chapters, "End of Book 1", dx.full_back(), [])
    out: list[dict] = [dict(title="Opening", items=[
        ("head", "The Ides of March."), ("head", "Book One."), ("head", f"By {AUTHOR}.")])]
    pending_act: str | None = None
    skipping = False
    i = 0
    while i < len(paras):
        text, role = paras[i]
        if role == "act":
            pending_act = text
        elif role == "chapter":
            title = speakable(paras[i + 1][0])
            items = []
            if pending_act:
                a, _, sub = pending_act.partition(":")
                items.append(("head", f"{a.strip()}. {speakable(sub)}."))
                pending_act = None
            items.append(("head", f"{text}."))
            items.append(("head", title.rstrip(".") + "."))
            label = text if text == "Prologue" else f"{text}: {title}"
            out.append(dict(title=label, items=items))
            skipping = False
            i += 2
            continue
        elif role == "back_head":
            # Historical note only; the timeline is a table for the eye.
            skipping = "historical" not in text.lower()
            if not skipping:
                out.append(dict(title=speakable(text), items=[("head", speakable(text) + ".")]))
        elif role == "end":
            out[-1]["items"].append(("head", "End of Book One."))
        elif skipping:
            pass
        elif role == "scene":
            out[-1]["items"].append(("scene", ""))
        elif role == "back_sub":
            out[-1]["items"].append(("head", speakable(text).rstrip(".") + "."))
        else:
            out[-1]["items"].append(("body", speakable(text)))
        i += 1
    for n, t in enumerate(out):
        t["n"] = n
    return out


def file_stem(t: dict) -> str:
    safe = re.sub(r"[^\w ,'’-]", "", t["title"]).strip()
    return f"{t['n']:02d} {safe}"[:80]


# --------------------------------------------------------------- audio ---

def fetch_model() -> None:
    MODELS.mkdir(parents=True, exist_ok=True)
    for f in MODEL_FILES:
        dest = MODELS / f
        if dest.exists():
            continue
        print(f"downloading {f} …", flush=True)
        urllib.request.urlretrieve(MODEL_URL + f, dest)


def engine(threads: int):
    import onnxruntime as rt
    from kokoro_onnx import Kokoro

    if not all((MODELS / f).exists() for f in MODEL_FILES):
        raise SystemExit("Model files missing: run with --fetch-model first.")
    opts = rt.SessionOptions()
    if threads:
        opts.intra_op_num_threads = threads
    sess = rt.InferenceSession(str(MODELS / MODEL_FILES[0]), opts, providers=["CPUExecutionProvider"])
    return Kokoro.from_session(sess, str(MODELS / MODEL_FILES[1]))


def phonemes(k, text: str) -> str:
    """Phonemise, swapping in LEXICON entries for the names."""
    out, pos = [], 0
    for m in _LEX_RE.finditer(text):
        before = text[pos:m.start()]
        if before.strip():
            out.append(k.tokenizer.phonemize(before, LANG))
        ph = LEXICON[m.group(1)]
        if m.group(2):
            ph += "ɪz" if ph[-1] in "szʃʒ" else ("s" if ph[-1] in "ptkfθ" else "z")
        out.append(ph)
        pos = m.end()
    rest = text[pos:]
    if rest.strip():
        out.append(k.tokenizer.phonemize(rest, LANG))
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def render_track(k, t: dict, voice: str, speed: float, wav: Path) -> float:
    import numpy as np
    import soundfile as sf

    def gap(s: float):
        return np.zeros(int(RATE * s), dtype=np.float32)

    chunks = [gap(0.4)]
    for kind, text in t["items"]:
        if kind == "scene":
            chunks.append(gap(SCENE_GAP - PARA_GAP))
            continue
        audio, _ = k.create(phonemes(k, text), voice=voice, speed=speed, lang=LANG, is_phonemes=True)
        chunks.append(audio.astype(np.float32))
        chunks.append(gap(HEAD_GAP if kind == "head" else PARA_GAP))
    chunks.append(gap(TRACK_TAIL))
    audio = np.concatenate(chunks)
    wav.parent.mkdir(parents=True, exist_ok=True)
    tmp = wav.with_suffix(".part.wav")
    sf.write(tmp, audio, RATE)
    tmp.replace(wav)
    return len(audio) / RATE


def ffmpeg(*args: str) -> None:
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def to_mp3(t: dict, wav: Path, mp3: Path, total: int, voice: str) -> None:
    mp3.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg("-i", str(wav), "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k",
           "-metadata", f"title={t['title']}", "-metadata", f"album={TITLE}",
           "-metadata", f"artist={AUTHOR}", "-metadata", f"track={t['n'] + 1}/{total}",
           "-metadata", "genre=Audiobook", "-metadata", f"comment=Kokoro TTS voice {voice}",
           str(mp3))


def duration(wav: Path) -> float:
    import soundfile as sf
    return sf.info(str(wav)).duration


def build_m4b(ts: list[dict], wavdir: Path, dest: Path, voice: str) -> None:
    lst = wavdir / "concat.txt"
    meta = wavdir / "chapters.txt"
    lines, ms = [";FFMETADATA1", f"title={TITLE}", f"artist={AUTHOR}", f"album={TITLE}",
                 "genre=Audiobook", f"comment=Kokoro TTS voice {voice}"], 0
    with lst.open("w") as f:
        for t in ts:
            wav = wavdir / f"{t['n']:02d}.wav"
            f.write(f"file '{wav.name}'\n")
            end = ms + int(round(duration(wav) * 1000))
            lines += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={ms}", f"END={end}", f"title={t['title']}"]
            ms = end
    meta.write_text("\n".join(lines) + "\n", encoding="utf-8")
    tmp = dest.with_suffix(".part.m4b")
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(meta), "-map_metadata", "1",
           "-map", "0:a", "-ac", "1", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart",
           "-f", "mp4", str(tmp))
    tmp.replace(dest)
    print(f"M4B: {dest} ({ms / 3600000:.2f} h, {len(ts)} chapters)")


SAMPLE = ("Chapter Fourteen. Brutus did not sleep. In the grey before dawn Porcia found him at the "
          "table, Cassius’s letter folded under his hand. Decimus would come at the second hour, "
          "and Cicero had sent nothing. It was the Ides of March.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--voice", default="bm_george")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--only", help="comma-separated track numbers (0 = opening, 1 = prologue …)")
    ap.add_argument("--threads", type=int, default=0)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--samples", action="store_true")
    ap.add_argument("--fetch-model", action="store_true")
    ap.add_argument("--m4b-only", action="store_true")
    ap.add_argument("--no-m4b", action="store_true")
    a = ap.parse_args()

    if a.fetch_model:
        fetch_model()
        return
    ts = tracks()
    if a.list:
        for t in ts:
            words = sum(len(x.split()) for _, x in t["items"])
            print(f"{t['n']:02d}  {words:6d}  {t['title']}")
        print(f"total words {sum(len(x.split()) for t in ts for _, x in t['items'])}")
        return

    k = engine(a.threads)
    if a.samples:
        import soundfile as sf
        from kokoro_onnx import Kokoro  # noqa: F401
        a.out.joinpath("samples").mkdir(parents=True, exist_ok=True)
        for v in BRITISH_VOICES:
            audio, _ = k.create(phonemes(k, SAMPLE), voice=v, speed=a.speed, lang=LANG, is_phonemes=True)
            wav = a.out / "samples" / f"sample_{v}.wav"
            sf.write(wav, audio, RATE)
            ffmpeg("-i", str(wav), "-c:a", "libmp3lame", "-b:a", "64k", str(wav.with_suffix(".mp3")))
            wav.unlink()
            print("sample", v)
        return

    wavdir = a.out / "wav"
    if not a.m4b_only:
        todo = ts if not a.only else [ts[int(n)] for n in a.only.split(",")]
        for t in todo:
            wav = wavdir / f"{t['n']:02d}.wav"
            mp3 = a.out / "mp3" / f"{file_stem(t)}.mp3"
            if not wav.exists():
                t0 = time.time()
                secs = render_track(k, t, a.voice, a.speed, wav)
                print(f"{t['n']:02d} {t['title'][:50]:50s} {secs / 60:6.1f} min audio "
                      f"in {(time.time() - t0) / 60:5.1f} min", flush=True)
            if not mp3.exists():
                to_mp3(t, wav, mp3, len(ts), a.voice)
    if not a.no_m4b and all((wavdir / f"{t['n']:02d}.wav").exists() for t in ts):
        build_m4b(ts, wavdir, a.out / "Ides_Book1_audiobook.m4b", a.voice)


if __name__ == "__main__":
    main()
