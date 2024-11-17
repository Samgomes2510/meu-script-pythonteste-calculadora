nano calculadora.sh
#!/bin/bash
echo "Escolha a operação: "
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"
read -p "Digite a opção (1-4): " operacao
read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

case $operacao in
  1) resultado=$(echo "$num1 + $num2" | bc);;
  2) resultado=$(echo "$num1 - $num2" | bc);;
  3) resultado=$(echo "$num1 * $num2" | bc);;
  4) resultado=$(echo "scale=2; $num1 / $num2" | bc);;
  *) echo "Opção inválida"; exit 1;;
esac

echo "O resultado é: $resultado"
chmod 744 calculadora.sh
./calculadora.sh