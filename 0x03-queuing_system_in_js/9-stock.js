import { createClient } from 'redis';
import express from 'express';

const app = express();
const client = createClient();

const listProducts = [
  {Id: 1, name: Suitcase 250, price: 50, stock: 4},
  {Id: 2, name: Suitcase 450, price: 100, stock: 10},
  {Id: 3, name: Suitcase 650, price: 350, stock: 2},
  {Id: 4, name: Suitcase 1050, price: 550, stock: 5}
];

const getItemById = (id) => {
  const list = listProducts.filter((item) => item.id == id);
  return list[0];
};


app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.listen(1245, () => {
  console.log('server is running');
});

const reserveStockById = (itemId, stock) => {
  client.hstet(itemId, stock);
});

const getCurrentReservedStockById = async (itemId) => {
  return client.get(itemId);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  getItemById(itemId);
});
