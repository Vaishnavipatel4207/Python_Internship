
#Project Title: Whois Lookup Tool

import whois

def whois_lookup(domain):
    try:
        whois_info = whois.whois(domain)
        print("Domain Name:", whois_info.domain_name)
        print("Registrar:", whois_info.registrar)
        print("Creation Date:", whois_info.creation_date)
        print("Expiration Date:", whois_info.expiration_date)
        print("Updated Date:", whois_info.updated_date)
        print("WHOIS Server:", whois_info.whois_server)
        print("Name Servers:",whois_info.name_servers)
        print("Status :",whois_info.status)
        print("Registrant Name:", whois_info.name)
        print("Registrant Email:", whois_info.emails)
        print("Registrant Organization:", whois_info.org)
        print("Address :",whois_info.address)
        print("City :",whois_info.city)
        print("State :",whois_info.state)
        print("Registrant Postal Code:",whois_info.registrant_postal_code)
        print("Registrant Country:", whois_info.country)
          
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    whois_lookup(domain)




