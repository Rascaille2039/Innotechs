/* 这一脚本提供了对TearUpTheSpace V2.3.α工业控制数字系统的管理员访问 */
/*  工业控制数字系统的访问链接是https://cyberinvestigation.fr/TUTS2_3_a/login */
		
/* 用户名和密码标记于下方的代码中 */

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
		group_admin*ID ->ngaccess = Admin001 	# 用于界面连接的默认用户名 
							
		group_admin*PassWord ->nbcryptPW = Password001 # 用于界面连接的默认密码 
								
	
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
