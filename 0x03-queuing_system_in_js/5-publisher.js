import { createClient } from 'redis';
/* module to publish to channel */


/* connect to redis */
const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/* if there is error during connection */
client.on('error', (err) => {
  console.log(err);
});

const channel = 'holberton school channel';

/* function used to pblish messages */
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log('About to send MESSAGE');
    client.publish(channel, message);
  }, time);
}

/* messages to publish */
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
