import os
from typing import List

import vlc

class AudioOutput:
  def __init__(self, audio_output_src="--aout=alsa"):
    self.instance = vlc.Instance(audio_output_src)  # NOTE: e.g. "--aout=alsa"
    self.player = vlc.MediaPlayer(self.instance)
    self.playing = False

  def play_audio_stream(self, audio_stream: List[str]) -> None:
    try:
      for audio_url in audio_stream:
        if audio_url:
          self.player.set_media(vlc.Media(audio_url))
          self.player.play()
          while self.player.get_state() == vlc.State.Opening: continue # NOTE: wait for the player to start playing
          while self.player.get_state() != vlc.State.Ended: continue  # NOTE: wait until playback is finished  
    except KeyboardInterrupt:
      self.player.stop()
      self.playing = False
      return
