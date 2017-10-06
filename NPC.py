
class NPC():
    def __init__(self, name):
        self.name = name
        self.hasFirstSpeech = False
        self.firstSpeechFinished = True

    def speech(self):
        raise NotImplementedError()

    def getName(self):
        return self.name


class PlayerMom(NPC):
    def __init__(self):
        self.hasfirstSpeech = True
        self.firstSpeechFinished = False
        super().__init__(name = "Mom")
        
    def firstSpeech(self):
        self.firstSpeechFinished = True
        return"""
        Right. All boys leave home some day. It said so on TV.
        PROF. OAK, next door, is looking for you."""
        
    def speech(self):
        return """
        RED! You should take a quick rest!
        [heal]
        Oh good! You and your Pokemon are looking great! Take care now!"""
        
