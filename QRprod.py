import qrcode
import qrcode.constants

code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2
)

link = input("Pleace paste your link: ")
code.add_data(link)
code.make(fit=True)
image=code.make_image(fill_color="black",back__color="white")
image.save('vol1.png')