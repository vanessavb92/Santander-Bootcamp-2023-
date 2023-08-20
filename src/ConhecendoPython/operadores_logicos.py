saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque
                                         )
