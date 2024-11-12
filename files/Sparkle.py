from files.Animation import Animation

def get_explosion_frames():
  frames = []
  for n in range(1, 16):
    frames.append((f"images/happy/happy{n}.png", 1))
    
  return frames

class Sparkle(Animation):
  def __init__(self, x, y):
    sequence = get_explosion_frames()
    super().__init__(x, y, sequence)
    self.play_mode = 'once'
