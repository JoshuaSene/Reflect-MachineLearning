import pymysql.cursors

con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_ia',
    port=3307,
    cursorclass=pymysql.cursors.DictCursor
)

cursor = con.cursor()
percepts = []


def showMainMenu():
    print('\n---------------------------------------------\n')
    print('Menu principal\n')

    print('\t1 - Rules Manager')
    print('\t2 - Purchases')
    print('\t3 - Quit')

    print('\n---------------------------------------------\n')



def startShoppingCart():
    percept = input('Informe o item da sua lista de compras: ')
    ## ask for a new item or eval
    print('actionE')

def getNumberInput(options, inputTitle='Selecione a opção do menu: '):
    inputValue = input(inputTitle)

    try:
        inputValue = int(inputValue)
        if inputValue <= len(options):
            return inputValue
        print('Opção inválida! Tente novamente')
    except:
        print('Opção inválida! Tente novamente')

    return getNumberInput(options, inputTitle)

def showManagementMenu():
    print('\n---------------------------------------------\n')
    print('\t1 - Create Rule')
    print('\t2 - Delete item')
    print('\t3 - Read rules')
    print('\t4 - Back to menu')
    print('\t5 - Quit')
    print('\n---------------------------------------------\n')

    options = {
            1: createRule,
            # 2: "deleteRule",
            3: listRules,
            4: showMainMenu,
            5: 'exitProject'
        }

    menuInput = getNumberInput(options)
    options[menuInput]()


def listRules():
    cursor.execute('SELECT * FROM rules')
    result = cursor.fetchall()
    print(result)

def createRule():
    relation = input("Inserir produto: ")
    action = input("Inserir acao: ")

    cursor.execute('INSERT INTO rules (relation, action_rules) VALUES ('+relation+', '+action+');')
    con.commit()

def deleteRule():
    relation = input("Inserir produto a ser excluido: ")
    action = input("Inserir acao a ser excluida: ")

    cursor.execute('DELETE FROM rules WHERE relation = ? and action_rules = ?)', format(relation, action))
    con.commit()


showManagementMenu()