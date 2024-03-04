import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

const asyncSet = promisify(client.set).bind(client);
const asyncGet = promisify(client.get).bind(client);

const setNewSchool = async (schoolName, value) => {
  try {
    const res = await asyncSet(schoolName, value);
    console.log(res);
  } catch (err) {
    console.log(err);
  }
}

const displaySchoolValue = async (schoolName) => {
  try {
    const res = await asyncGet(schoolName);
    console.log(res);
  } catch (err) {
    console.log(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
