
echo "local:"
ls 

echo "device:"
ls /pyboard

echo "removing pico files"
rm /pyboard/*

echo "should now be empty:"
ls pyboard

echo "deploy new code..."
cp *.py /pyboard/

echo "should now be have new code:"
ls /pyboard

echo "restart the pico"
repl ~ machine.reset()~

