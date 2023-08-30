import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask

qr = qrcode.QRCode(version=5,
                   mask_pattern=1,#7
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)
qr.add_data("ST00012|Name=ООО \"Актив Центр\"|PersonalAcc=40702810790450002405|BankName=ПАО \
            «Банк „Санкт-Петербург“|BIC=044030790|CorrespAcc=30101810900000000790|PayeeINN=7840095579\
            |KPP=044030790|Purpose=Перевод по договору займа|TechCode=12|Sum=100000")


img = qr.make_image(image_factory=StyledPilImage,
                      module_drawer=RoundedModuleDrawer(radius_ratio=1),
                      eye_drawer=RoundedModuleDrawer(radius_ratio=1),
                      color_mask=RadialGradiantColorMask(back_color=(222, 246, 74),
                                                         center_color=(100, 100, 100),
                                                         edge_color=(0, 0, 0)),
                      embeded_image_path="activ-logo-noback.png")


img.save("qr.png")
