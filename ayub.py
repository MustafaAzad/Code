import base64

encoded_text = "8K/IEjCxfNrzUu9VDJSZWD++tiaO120L751GVSpHpHWMH/9dcq8l0iAAxVvzEkguLSRrcrqoQPzU"
decoded_bytes = base64.b64decode(encoded_text)
print(decoded_bytes)