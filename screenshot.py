import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'))
from PIL import ImageGrab
snapshot = ImageGrab.grab()
save_path = "ss.jpg"
snapshot.save(save_path)
