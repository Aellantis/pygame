from files.Animation import Animation

def get_explosion_frames():
  frames = []
  for n in range(1, 21):
    frames.append((f"images/question/q{n}.png", 1))
    
  return frames

class Explosion(Animation):
  def __init__(self, x, y):
    sequence = get_explosion_frames()
    super().__init__(x, y, sequence)
    self.play_mode = 'once'
