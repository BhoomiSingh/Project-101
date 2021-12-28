import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.A_DrWqBOpAWm2uCv2-YkPk3HoDWJQyRMM-u5Qd-wMv318dlGFj3t9qHplht7TE2zx4o2x_B8i7DXh4fL1naw5bVFOMUNZqeTZLuvY5CF5xrkMTuaDDk2m-uO_TCrXDR5pJWd8EL1qXA'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : ")
    file_to = input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")
main()
