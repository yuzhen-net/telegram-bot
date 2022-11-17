import os


if __name__ == '__main__':
    with open('yznet-bot/.env.dev', 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('REPLACE_TO_API_KEY_AUTOMATICLY', os.environ['TELEGRAM_API_KEY'])
    with open('yznet-bot/.env.dev', 'w', encoding='utf-8') as f:
        f.write(content)
