class Image:
    def __init__(self, index):
        self.image_name = f"{index}.gif"
        self.image_path = f"images/{index}.gif"

    def getImagePath(self):
        return self.image_path

    def getImageName(self):
        return self.image_name
