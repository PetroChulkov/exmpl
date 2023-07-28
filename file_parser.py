from pathlib import Path

IMAGE = []
VIDEO = []
DOCS = []
AUDIO = []
ARCHIVE = []
MY_OTHER = []


REGISTER_EXTENSIONS = {
    'JPEG': IMAGE, 'JPG': IMAGE, 'SVG': IMAGE, 'PNG': IMAGE,
    'AVI': VIDEO, 'MP4': VIDEO, 'MOV': VIDEO, 'MKV': VIDEO,
    'DOC': DOCS, 'DOCX': DOCS, 'TXT': DOCS, 'PDF': DOCS, 'XLSX': DOCS, 'PPTX': DOCS,
    'MP3': AUDIO, 'OGG': AUDIO, 'WAV': AUDIO, 'AMR': AUDIO,
    'ZIP': ARCHIVE, 'GZ': ARCHIVE, 'TAR': ARCHIVE, 'RAR': ARCHIVE,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)
