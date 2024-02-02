# Tanımlar
Prx_exist = -121  # dBm
SMA_CONNECTOR_LOSS = 1  # dB
RG58_CABLE_LOSS = 1  # 1dB per meter
CABLE_LENGTH = 0.0  # meter

#Link Bütçesi Hesabı Wikipedia: https://en.wikipedia.org/wiki/Link_budget

# Vericinin çıkış gücü (dBm)
Ptx = 30

# Vericinin anten kazancı (dBi)
Gtx = 3

# Vericinin kayıpları (coax, connectors...) (dB)
Ltx = SMA_CONNECTOR_LOSS

# Kayıplar (dB) Boş uzay kaybı
Lfs = 115.2454  # freespacepathloss.py dosyasında hesaplanması var

# Çeşitli Kayıplar (dB) (Solma marjı, vücut kaybı, polarizasyon uyumsuzluğu, diğer kayıplar, ...)
Lm = 5  # Polarization errors

# Alıcı anten kazancı (dBi)
Grx = 3

# Alıcının kayıpları (coax, connectors...) (dB)
Lrx = SMA_CONNECTOR_LOSS + (RG58_CABLE_LOSS * CABLE_LENGTH)

# Alıcı gücünün hesaplanması (dBm) Friis Denklemi
Prx = Ptx + Gtx - Ltx - Lfs + Grx - Lrx - Lm

# Mevcut Güç
Prx_total = Prx + Prx_exist

print("Received power (dBm):", Prx_total)