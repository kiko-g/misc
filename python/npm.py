import sys


"""
"""
def npm_latest(npm_outdated_content: list, operation: str = 'latest'):
    result = []
    
    for line in npm_outdated_content:
        if line.startswith('Package'):
            continue

        package, current, wanted, latest, location, _ = line.split()
        if current != latest:
            if operation == 'latest':
                result.append(f'npm i {package}@latest')

            elif operation == 'info':
                result.append(f'{package} {current} -> {latest}')
    
    return result


# Usage: npm outdated | python npm.py
if __name__ == '__main__':
    separator = ' ; '
    npm_outdated_content = []
    for line in sys.stdin:
        npm_outdated_content.append(line.strip())

    latest = npm_latest(npm_outdated_content)
    update_all = separator.join(latest)
    
    print(update_all)
