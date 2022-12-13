def main(cmds='plain bold italic header link inline-code new-line ordered-list unordered-list !help !done'):
    while (cmd := input('Choose a formatter: ')) not in cmds.split():
        print('Unknown formatting type or command')
    if cmd == '!help':
        print(f'Available formatters: {cmds[:78]}\nSpecial commands: {cmds[79:]}')
    else:
        result.append(globals()[cmd.replace('-', '_').replace('!', '')]())
        print(*result, sep='')
    main()


def plain():
    return input('Text: ')


def bold():
    return input('Text: ').join(('**', '**'))


def italic():
    return input('Text: ').join(('*', '*'))


def header(level=0):
    while level not in range(1, 7):
        try:
            assert (level := int(input('Level: '))) in range(1, 7)
        except (ValueError, AssertionError):
            print('The level should be within the range of 1 to 6')
    return '{} {}\n'.format('#' * level, input('Text: '))


def link():
    return '[{}]({})'.format(input('Label: '), input('URL: '))


def inline_code():
    return input('Text: ').join(('`', '`'))


def new_line():
    return '\n'


def ordered_list(sym='.', n_rows=0):
    while n_rows <= 0:
        try:
            assert (n_rows := int(input('Number of rows: '))) > 0
        except (ValueError, AssertionError):
            print('The number of rows should be greater than zero')
    return ''.join(f"{str(n) + sym} {input(f'Row #{n}: ')}\n" for n in range(1, n_rows + 1))


def unordered_list():
    return ordered_list('\r*')


def done():
    with open('output.md', 'w') as f:
        print(*result, sep='', end='', file=f)
    exit()


result = []
main()
