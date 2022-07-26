## QR Demo

Demo app for printing QR Codes.

This app contains a DocType **QR Demo**. You can create a new **QR Demo**, fill the _Title_ field and save.

In the backend, the title is converted to a QR code image with these steps:

1. Create QR code, using https://pypi.org/project/qrcode/
2. Convert the raw bytes of QR code to a base64 encoded string
3. Add info about filetype and encoding for the browser
4. Save the QR Code data in the field _QR Code_

![Form: saved QR Demo](img/form.png)

The **QR Demo** DocType also has a field _QR Image_, which just displays the data stored in _QR Code_.

> Note: In a production application, you'll want to set the field _QR Code_ as hidden, so the user doesn't see the raw data.

Try to print the document, using the print format "QR Demo". The QR code will work flawlessly in print preview and PDF. The print format is very simple. It uses the data from _QR Code_ like this:

```jinja
<p>QR Code with content "{{ doc.title }}":</p>
<img src="{{ doc.qr_code }}" alt="{{ doc.title }}"/>
```

### Print Preview
![Form: saved QR Demo](img/print_preview.png)

### Print PDF
![Form: saved QR Demo](img/print_pdf.png)
