import qrcode

# QR 코드로 만들 깃허브 URL
url = "https://https://github.com/sidebar12/lastfinal"  # ← 여기에 실제 깃허브 주소 넣으세요

# QR 코드 생성
qr = qrcode.make(url)

# 이미지로 저장
qr.save("github_qr.png")

print("QR 코드가 'github_qr.png'로 저장되었습니다.")
