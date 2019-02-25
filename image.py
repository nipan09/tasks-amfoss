from PIL import Image
oswal= Image.open('oswald.png')
oswal.rotate(270).save('os.png')
from PIL import Image
oswal= Image.open('os.png')
oswal = oswal.convert('1')
oswal.save('np.png')
