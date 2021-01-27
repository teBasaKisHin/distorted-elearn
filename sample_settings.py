url = {
    'login': 'https://k-mdl01.kure-nct.ac.jp/login/index.php',
    'date_list': 'https://k-mdl01.kure-nct.ac.jp/course/view.php?id=6',
    'input': 'https://k-mdl01.kure-nct.ac.jp/mod/feedback/complete.php?courseid&gopage=0&id=',
    'submit': 'https://k-mdl01.kure-nct.ac.jp/mod/feedback/complete.php?'
}

payload = {
    'login': {
        # Set up your account.
        'username': 'admin',
        'password': 'password',
        # Dont need to edit.
        'anchor': ''
    }
}

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) Chrome/87.0.4280.66'
}

