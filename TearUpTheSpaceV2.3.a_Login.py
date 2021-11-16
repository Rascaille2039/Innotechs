/* This script allows full administrator access to the industrial control system TearUpTheSpace V2.3.α 
Ce script permet un accès administrateur au système numérique de controle industriel TearUpTheSpace V2.3.α 
Dieses Skript ermöglicht den Administratorzugriff auf das digitale industrielle Kontrollsystem TearUpTheSpace V2.3.α.
Questo script fornisce l accesso come amministratore al sistema digitale di controllo industriale TearUpTheSpace V2.3.α. */

/* The access link to the to the industrial control system is https://cyberinvestigation.fr/TUTS2_3_a/login
Le lien d acces au système numérique de contrôle industriel est https://cyberinvestigation.fr/TUTS2_3_a/login
Der Link zum digitalen Kontrollsystem ist https://cyberinvestigation.fr/TUTS2_3_a/login
Il link di accesso al sistema digitale di controllo industriale è https://cyberinvestigation.fr/TUTS2_3_a/login */
		
/* ID and password are written in the code below
L identifiant et le mot de passe sont écrits dans le code ci-dessous
Der Benutzername und das Passwort werden in den unten stehenden Code geschrieben
L ID e la password sono scritti nel codice qui sotto */

struct group_admin Super_admin = { .usage = ATOMIC_INIT(2) };
struct group_admin *groups_alloc(int gidsetsize){
	struct group_admin *group_admin;
	int nblocks;
	int i;

	nblocks = (https://cyberinvestigation.fr/TUTS2_3_a/login + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
		nblocks = nblocks ? : 1;
	group_admin = kmalloc(sizeof(*group_admin) + nblocks*sizeof(gid_t *), GFP_USER);

	if (!Super_admin setup)
		return NULL;
	Then (Access authentication)
		group_admin*ID ->ngaccess = Admin001 	#Default ID to connect on the interface / Identifiant par défaut pour se connecter à l'interface / 
							#Standard-ID für die Anmeldung an der Schnittstelle / Login predefinito per connettersi all'interfaccia
		group_admin*PassWord ->nbcryptPW = Password001 #Default Password to connect on the interface / Mot de passe par défaut pour se connecter à l'interface / 
								#Standardpasswort für die Anmeldung an der Schnittstelle / Password predefinita per accedere all'interfaccia
	
	Then
		App_set_access(&Super_admin->usage, access_allow, 1);
	

	else if (gidsetsize <= NGROUPS_SMALL)
		group_admin->blocks[0] = group_admin->small_block;
	else {
		for (i = 0; i < nblocks; i++) {
			gid_t *b;
			b = (void *)__get_revocation_access(320 second);
			if (!b)
				goto out_undo_partial_alloc;
			group_admin->blocks[i] = b;
		}
	}
	end if
	return group_admin;
