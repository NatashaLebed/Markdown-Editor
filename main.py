def plain(txt):
    return txt


def bold(txt):
    return f'**{txt}**'


def italic(txt):
    return f'*{txt}*'


def inline_code(txt):
    return f"`{txt}`"


def new_line():
    return '\n'


def header():
    level = int(input('- Level:'))
    if level not in range(1, 7):
        print('The level should be within the range of 1 to 6')
    txt = input('- Text:')
    return '#' * level + f' {txt}\n'


def link():
    label = input('- Label:')
    url = input('- URL:')
    return f'[{label}]({url})'


def md_list():
    all_list_items = ''
    n = int(input('Number of rows:'))
    while n < 1:
        print('The number of rows should be greater than zero')
        n = int(input('Number of rows:'))
    for i in range(1, n + 1):
        list_item = input(f'Row #{i}:')
        sign = '*' if command == 'unordered-list' else f'{i}.'
        all_list_items += f'{sign} {list_item}\n'
    return all_list_items


markdown = []

while True:
    command = input('- Choose a formatter:')

    if command == '!done':
        with open('output.md', 'w') as f:
            f.write(''.join(markdown))
        break
    elif command == 'plain':
        text = plain(input('- Text:'))
    elif command == 'bold':
        text = bold(input('- Text:'))
    elif command == 'italic':
        text = italic(input('- Text:'))
    elif command == 'inline-code':
        text = inline_code(input('- Text:'))
    elif command == 'new-line':
        text = new_line()
    elif command == 'header':
        text = header()
    elif command == 'link':
        text = link()
    elif command == 'ordered-list' or command == 'unordered-list':
        text = md_list()
    elif command == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
    else:
        print('Unknown formatting type or command')

    markdown.append(text)
    for item in markdown:
        print(item, end='')
    print()
