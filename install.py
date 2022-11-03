import helpers

def installPhpDialog(packages):
    avail_php_vers = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0']
    avail_php_vers_str = ','.join(map(str, avail_php_vers))
    sel_php_vers = []

    print("Enter PHP version to install: [" + avail_php_vers_str + "]")
    # i = 0
    while True:
        ver = input()
        if ver == "":
            if len(sel_php_vers) > 0:
                break
            else:
                print("You must select at least one version!")
                print("Enter PHP version to install: [" + avail_php_vers_str + "]")
        else:
            if avail_php_vers.count(ver) > 0:
                sel_php_vers.append(ver)
                print("Enter another one PHP version to install or leave empty for finish: [" + avail_php_vers_str + "]")
            else:
                print("Enter correct PHP version to install: [" + avail_php_vers_str + "]")

    for ver in sel_php_vers:
        match ver:
            case "5.6":
                packages.append("php5.6 php5.6-common php5.6-cgi php5.6-fpm php5.6-cli php5.6-dev php5.6-bcmath php5.6-mbstring php5.6-curl php5.6-soap php5.6-interbase php5.6-mysql php5.6-pgsql php5.6-sqlite3 php5.6-odbc php5.6-dba php5.6-bz2 php5.6-zip php5.6-json php5.6-xml php5.6-xsl php5.6-phpdbg php5.6-pspell php5.6-readline php5.6-sybase php5.6-tidy php5.6-enchant php5.6-gmp php5.6-imap php5.6-intl php5.6-gd php5.6-imagick")
            case "7.0":
                packages.append("php7.0 php7.0-common php7.0-cgi php7.0-fpm php7.0-cli php7.0-dev php7.0-bcmath php7.0-mbstring php7.0-curl php7.0-soap php7.0-interbase php7.0-mysql php7.0-pgsql php7.0-sqlite3 php7.0-odbc php7.0-dba php7.0-bz2 php7.0-zip php7.0-json php7.0-xml php7.0-xsl php7.0-phpdbg php7.0-pspell php7.0-readline php7.0-sybase php7.0-tidy php7.0-enchant php7.0-gmp php7.0-imap php7.0-intl php7.0-gd php7.0-imagick")
            case "7.1":
                packages.append("php7.1 php7.1-common php7.1-cgi php7.1-fpm php7.1-cli php7.1-dev php7.1-bcmath php7.1-mbstring php7.1-curl php7.1-soap php7.1-interbase php7.1-mysql php7.1-pgsql php7.1-sqlite3 php7.1-odbc php7.1-dba php7.1-bz2 php7.1-zip php7.1-json php7.1-xml php7.1-xsl php7.1-phpdbg php7.1-pspell php7.1-readline php7.1-sybase php7.1-tidy php7.1-enchant php7.1-gmp php7.1-imap php7.1-intl php7.1-gd php7.1-imagick")
            case "7.2":
                packages.append("php7.2 php7.2-common php7.2-cgi php7.2-fpm php7.2-cli php7.2-dev php7.2-bcmath php7.2-mbstring php7.2-curl php7.2-soap php7.2-interbase php7.2-mysql php7.2-pgsql php7.2-sqlite3 php7.2-odbc php7.2-dba php7.2-bz2 php7.2-zip php7.2-json php7.2-xml php7.2-xsl php7.2-phpdbg php7.2-pspell php7.2-readline php7.2-sybase php7.2-tidy php7.2-enchant php7.2-gmp php7.2-imap php7.2-intl php7.2-gd php7.2-imagick")
            case "7.3":
                packages.append("php7.3 php7.3-common php7.3-cgi php7.3-fpm php7.3-cli php7.3-dev php7.3-bcmath php7.3-mbstring php7.3-curl php7.3-soap php7.3-interbase php7.3-mysql php7.3-pgsql php7.3-sqlite3 php7.3-odbc php7.3-dba php7.3-bz2 php7.3-zip php7.3-json php7.3-xml php7.3-xsl php7.3-phpdbg php7.3-pspell php7.3-readline php7.3-sybase php7.3-tidy php7.3-enchant php7.3-gmp php7.3-imap php7.3-intl php7.3-gd php7.3-imagick")
            case "7.4":
                packages.append("php7.4 php7.4-common php7.4-cgi php7.4-fpm php7.4-cli php7.4-dev php7.4-bcmath php7.4-mbstring php7.4-curl php7.4-soap php7.4-interbase php7.4-mysql php7.4-pgsql php7.4-sqlite3 php7.4-odbc php7.4-dba php7.4-bz2 php7.4-zip php7.4-json php7.4-xml php7.4-xsl php7.4-phpdbg php7.4-pspell php7.4-readline php7.4-sybase php7.4-tidy php7.4-enchant php7.4-gmp php7.4-imap php7.4-intl php7.4-gd php7.4-imagick")
            case "8.0":
                packages.append("php8.0 php8.0-common php8.0-cgi php8.0-fpm php8.0-cli php8.0-dev php8.0-bcmath php8.0-mbstring php8.0-curl php8.0-soap php8.0-interbase php8.0-mysql php8.0-pgsql php8.0-sqlite3 php8.0-odbc php8.0-dba php8.0-bz2 php8.0-zip php8.0-xml php8.0-xsl php8.0-phpdbg php8.0-pspell php8.0-readline php8.0-sybase php8.0-tidy php8.0-enchant php8.0-gmp php8.0-imap php8.0-intl php8.0-gd php8.0-imagick")

    return packages

def installPackagesDialog():
    packages = ['nginx']

    print("Install apache2: [Y/n]")
    if 'y' == helpers.boolQuestion("y"):
        packages.append('apache')

    print("Install certbot: [Y/n]")
    if 'y' == helpers.boolQuestion("y"):
        packages.append('certbot')

    packages = installPhpDialog(packages)

    installPackages(packages)
    return

def installPackages(packages):
    print("Packages to install:")
    print(packages)
    #ToDo
    return