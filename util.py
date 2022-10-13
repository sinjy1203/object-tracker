class login:
    def __init__(self, init_detect, init_range):
        self.init_detect = init_detect
        self.init_range = init_range
        self.user = None
        self.x = None

    def location(self, bbox):
        self.x = round(319.5 - (int(bbox[0]) + int(bbox[2])) / 2)

    def detect(self, class_name, track):
        if not self.init_detect:
            if class_name == "person" and - self.init_range <= self.x <= self.init_range:
                self.user = track.track_id
                self.init_detect = True

        if class_name == "person" and track.track_id == self.user:
            return self.x

        return None