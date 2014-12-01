Instructions: - 
1. Copy the boat folder to following location: 
	~/.pyenv/versions/barbican27/lib/site-packages/
2. Cd to boat/
3. run command: python setup.py install
4. Append the namespace changes from barbican-api.conf to local /etc/barbican/barbican-api.conf file

# ================= Attestation plugin ===================
[attester]
namespace = boat.attestation.attester
enabled_attester_plugins = simple_attest



