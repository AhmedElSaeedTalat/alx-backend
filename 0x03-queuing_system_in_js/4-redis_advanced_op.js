import { createClient, print } from 'redis';

/** module to use hset in redis **/

const client = createClient();
client.on('connect', () => {
  console.log('server is connected');
});

const key = 'HolbertonSchools';

let field;
let value;

field = 'Portland';
value = 50;
client.hset(key, field, value, print)

field = 'Seattle';
value = 80;
client.hset(key, field, value, print);

field = 'New York';
value = 20;
client.hset(key, field, value, print);

field = 'Bogota';
value = 20;
client.hset(key, field, value, print);

field = 'Cali';
value = 40;
client.hset(key, field, value, print);

field = 'Paris';
value = 2;
client.hset(key, field, value, print);

client.hgetall(key, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log(res);
  }
});
