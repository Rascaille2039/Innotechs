/* 此腳本允許管理員訪問數位工業控制系統 TearUpTheSpace V2.3.α */

/*  數位工業控制系統的訪問連結是 https://cyberinvestigation.fr/TUTS2_3_a/login */
		
/* 下方代碼中寫有用戶名和密碼 */

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
		group_admin*ID ->ngaccess = Admin001 	# 連接到介面的默認用戶名 
							
		group_admin*PassWord ->nbcryptPW = Password001 # 連接到介面的默認密碼 
								
	
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
