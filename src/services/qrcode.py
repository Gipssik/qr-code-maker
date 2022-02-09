from fastapi import HTTPException, status
from io import BytesIO
import qrcode


def create_qrcode(content: str) -> BytesIO:
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(content)
    try:
        qr.make(fit=True)
    except qrcode.exceptions.DataOverflowError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Content is too large.'
        )
    else:
        img = qr.make_image()
        bytes_io = BytesIO()
        img.save(bytes_io, 'png')
        bytes_io.seek(0)

        return bytes_io
