from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os, pickle
from googleapiclient.http import MediaFileUpload

# Configuração das credenciais e do escopo
SCOPES = ['https://www.googleapis.com/auth/drive']
creds = None
folder_id = '1CKdb9DwuAtPktdGx7CigmXW1KPL9CLFS'

# O arquivo token.pickle armazena os tokens de acesso e atualização do usuário, e é
# criado automaticamente quando o fluxo de autorização é concluído pela primeira vez.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

# Se não há credenciais válidas disponíveis, o usuário deve fazer login.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret_359458515747-s7t6bp5fm517pvcdpqk7i0g3ebietv4n.apps.googleusercontent.com.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Chama a API do Google Drive
service = build('drive', 'v3', credentials=creds)


# deletar todos os aquivos da pasta
items = service.files().list(q=f"'{folder_id}' in parents").execute()['files']
for item in items:
    service.files().delete(fileId=item['id']).execute()
    print(f"Arquivo {item['name']} deletado com sucesso!")

# upload dos arquivos da pasta downloads
for filename in os.listdir('downloads'):
    file_path = os.path.join('downloads', filename)
    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Arquivo {filename} enviado com sucesso!")