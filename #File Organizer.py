from pathlib import Path
path = Path(input('Please enter the folder that you want to organize into: '))

for item in path.iterdir():

    if item.is_file():
        if item.suffix =='.mp3':
            audios = path / "Audios"
            audios.mkdir(exist_ok=True)

            newaud = audios/item.name
            item.rename(newaud)

        elif item.suffix =='.mp4':
            videos = path / "Videos"
            videos.mkdir(exist_ok=True)

            newvid = videos/item.name
            item.rename(newvid)

        elif item.suffix in ['.jpg', '.jpeg' ,'.png']:
            images = path / "Images"
            images.mkdir(exist_ok=True)

            newimg = images / item.name
            item.rename(newimg)

        elif item.suffix == ['.pdf', '.docx', '.txt']:
            documents = path / "Documents"
            documents.mkdir(exist_ok=True)

            newdoc = documents / item.name
            item.rename(newdoc)

        else:
            others = path / "Others"
            others.mkdir(exist_ok=True)

            newoth = others / item.name
            item.rename(newoth)

    