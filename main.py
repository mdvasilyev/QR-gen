import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

qr = qrcode.QRCode(version=5,
                   mask_pattern=7,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=20,
                   border=2)
qr.add_data("https://t.me/mdvasilyev")


img = qr.make_image(image_factory=StyledPilImage,
                      module_drawer=RoundedModuleDrawer(radius_ratio=1),
                      eye_drawer=RoundedModuleDrawer(radius_ratio=1),
                      color_mask=SolidFillColorMask(back_color=(222, 246, 74), front_color=(0, 0, 0)),
                      embeded_image_path="activ-logo-noback.png")


img.save("qr.png")
