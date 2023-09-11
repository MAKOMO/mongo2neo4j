const mongoose = require('mongoose');
const {User, Product, Order, Countries} = require('./models');

const NUM_USERS = 100;
const NUM_COUNTRIES = 10;
const NUM_ORDERS = 300;
const NUM_PRODUCTS = 1000;

const countries = [
    'Germany', 'France', 'Italy', 'Spain', 'United Kingdom',
    'Netherlands', 'Belgium', 'Switzerland', 'Sweden', 'Austria'
];

const categories = ['food', 'beverages', 'cosmetics', 'electronics', 'toys'];

const fantasyProductNames = [
    'Mystic Elixir', 'Galactic Nectar', 'Enchanted Glow', 'Quantum Spark', 'Ethereal Delight',
    'Luminary Potion', 'Celestial Brew', 'Cosmic Mirage', 'Infinite Shimmer', 'Astral Wonder',
    // ... Add more fantasy names
];

const fantasyUserNames = [
    'Sirius', 'Luna', 'Aurora', 'Orion', 'Nova',
    'Stella', 'Solstice', 'Zephyr', 'Thalia', 'Titania',
    // ... Add more fantasy names
];

const fantasyLastNames = [
    'Arrington', 'Dixon', 'Bennett', 'Eastwood', 'Kirby',
    'Willow', 'Hightower', 'Youngblood', 'Yates', 'Steele', 'Peterson',
    // ... Add more fantasy names
];

const subscriptionTypes = [ 'free', 'home', 'pro'];

async function generateDummyData() {

    // Create countries
    const cntrs = [];
    for (let i = 0; i < countries.length; i++) {
        cntrs.push({
            isoname: countries[i],
        })
    }
    await Countries.insertMany(cntrs);

    // Create users
    const users = [];
    for (let i = 0; i < NUM_USERS; i++) {
        users.push({
            name: fantasyUserNames[i % fantasyUserNames.length],
            lastname: fantasyLastNames[i % fantasyLastNames.length],
            email: `user${i}@example.com`,
            country: countries[i % NUM_COUNTRIES],
            subscription: subscriptionTypes[Math.floor(Math.random() * Math.random() * (subscriptionTypes.length + 1))],
        });
    }
    await User.insertMany(users);

    // Create products
    const products = [];
    for (let i = 0; i < NUM_PRODUCTS; i++) {
        products.push({
            name: fantasyProductNames[i % fantasyProductNames.length],
            category: categories[Math.floor(Math.random() * categories.length)],
        });
    }
    await Product.insertMany(products);

    const userDBObjects = await User.find();
    const productDBObjects = await Product.find();

    // Create orders
    for (let i = 0; i < NUM_ORDERS; i++) {
        const userIndex = Math.floor(Math.random() * NUM_USERS);
        const user = userDBObjects[userIndex];
        const orderDate = new Date(`2022-${Math.floor(Math.random() * 12) + 1}-${Math.floor(Math.random() * 28) + 1}`);
        const numProducts = Math.floor(Math.random() * 10) + 1;
        const orderProducts = [];
        for (let j = 0; j < numProducts; j++) {
            const prodIdx = Math.floor(Math.random() * NUM_PRODUCTS);
            const product = productDBObjects[prodIdx];
            const productId = product._id;
            const quantity = Math.floor(Math.random() * 5) + 1;
            orderProducts.push({productId, quantity});
        }
        const order = await Order.create({user: user._id, products: orderProducts, orderDate});
        await order.save();
    }

    console.log('Dummy data generated successfully.');
}

// Parameters for host, port, and database
const host = process.argv[2] || 'localhost';
const port = process.argv[3] || '27017';
const database = process.argv[4] || 'mydatabase';

mongoose.connect(`mongodb://${host}:${port}/${database}`, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});
mongoose.connection.once('open', async () => {
    await generateDummyData();
    mongoose.connection.close();
});
