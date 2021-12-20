import dropbox
class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
        
    def uploadfiles(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accesstoken)
        f = open (filefrom,'rb')
        dbx.files_upload(f.read(),fileto)
    
def main():
    accesstoken = 'sl.A-Fzk_hDJKCI3n4ZhUz80zE-3CQ5njHzkD9C264B_D1rzouu7iNFqiVX8vXXw0jGIqo0rPIhv4ekHJ8MkB50Argt_ge0U7wvPitM71vbF2kYOUJlVJv2mEtcmHNbb2Tq9UOPjLo'
    transferdata = Transferdata(accesstoken)
    filefrom = 'C:\Users\nasir\Desktop\Python\example.txt'
    fileto = 'C:\Users\nasir\Dropbox\folder\way.txt'
    transferdata.uploadfiles(filefrom,fileto)
    print('file has been moved')
    
main()
        
