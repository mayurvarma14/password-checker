from password_checker import check_password


def main():
    password = input('Enter a password to check if it\'s leaked: ')
    count = check_password(password)
    if count:
        print(f'This password is leaked {count} times!')
    else:
        print('This password is not leaked \N{grinning face} ')


if __name__ == '__main__':
    main()
