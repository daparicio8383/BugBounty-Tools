import requests
from requests.exceptions import RequestException, ConnectionError, SSLError
from datetime import datetime

# Lista de dominios
domains = ["maps.google.com","support.google.com","play.google.com","bbb.plus.google.com","docs.google.com","drive.google.com","developers.google.com","bbb.policies.google.com","accounts.google.com","sites.google.com","mail.google.com","calendar.google.com","apis.google.com","chrome.google.com","news.google.com","analytics.google.com","tools.google.com","ads.google.com","cloud.google.com","translate.google.com","code.google.com","groups.google.com","myaccount.google.com","search.google.com","services.google.com","transparencyreport.google.com","scholar.google.com","books.google.com","podcasts.google.com","script.google.com","marketingplatform.google.com","photos.google.com","workspace.google.com","fonts.google.com","gsuite.google.com","trends.google.com","families.google.com","landing.google.com","firebase.google.com","takeout.google.com","myactivity.google.com","artsandculture.google.com","patents.google.com","cse.google.com","jigsaw.google.com","business.google.com","picasaweb.google.com","adwords.google.com","productforums.google.com","account.google.com","pay.google.com","hangouts.google.com","earth.google.com","meet.google.com","console.cloud.google.com","store.google.com","privacy.google.com","adssettings.google.com","images.google.com","datastudio.google.com","video.google.com","console.developers.google.com","get.google.com","profiles.google.com","mapsengine.google.com","colab.research.google.com","feedburner.google.com","assistant.google.com","spreadsheets.google.com","careers.google.com","contacts.google.com","issuetracker.google.com","tagmanager.google.com","lookerstudio.google.com","research.google.com","encrypted.google.com","region1.analytics.google.com","vr.google.com","one.google.com","edu.google.com","classroom.google.com","keep.google.com","bard.google.com","fi.google.com","feedproxy.google.com","apps.google.com","sheets.google.com","adsense.google.com","console.firebase.google.com","safebrowsing.google.com","dl.google.com","security.google.com","payments.google.com","picasa.google.com","jobs.google.com","fiber.google.com","stadia.google.com","codelabs.developers.google.com","voice.google.com","local.google.com"]

results = []

print("Testing...\n")
for domain in domains:
    url = f"https://{domain}"
    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
        status = f"HTTP {response.status_code}"
    except ConnectionError as e:
        if 'Connection reset' in str(e):
            status = "Connection reset"
        else:
            status = "Connection error"
    except SSLError:
        status = "SSL error"
    except RequestException as e:
        status = f"Other error - {type(e).__name__}"

    # Guardar y mostrar en tiempo real
    results.append((domain, status))
    print(f"{domain}: {status}")

# Función para ordenar por código HTTP numérico o poner los errores al final
def sort_key(item):
    domain, status = item
    if status.startswith("HTTP"):
        try:
            return (0, int(status.split()[1]))  # (grupo 0 = Código de estado HTTP)
        except ValueError:
            return (0, 9999)
    else:
        return (1, status)  # (grupo 1 = errores, orden alfabético entre ellos)

# Ordenar resultados
results.sort(key=sort_key)

# Crear archivo con nombre basado en la fecha actual
filename = datetime.now().strftime("%d_%m_%Y") + ".txt"
with open(filename, "w") as f:
    for domain, status in results:
        f.write(f"{domain}: {status}\n")

print("\nResults:\n")
for domain, status in results:
    print(f"{domain}: {status}")

print(f"\nResults saved in: {filename}")

