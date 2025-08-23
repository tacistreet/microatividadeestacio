def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-Vindo, Administrador')
    else:
        print('Bem-vindo Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('etc')