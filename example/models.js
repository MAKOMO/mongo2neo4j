const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    lastname: String,
    email: String,
    country: String,
    subscription: String,
});

const User = mongoose.model('User', userSchema);

const countrySchema = new mongoose.Schema({
    isoname: String,
});

const Countries = mongoose.model('Countries',countrySchema);

const productSchema = new mongoose.Schema({
    name: String,
    category: String,
});

const Product = mongoose.model('Product', productSchema);


const productOrderSchema = new mongoose.Schema(
    {
        productId: {type: mongoose.Schema.Types.ObjectId, ref: 'Product'},
        quantity: Number
    },
    {_id: false}
);

const orderSchema = new mongoose.Schema({
    user: {type: mongoose.Schema.Types.ObjectId, ref: 'User'},
    products: [productOrderSchema],
    orderDate: Date,
});

const Order = mongoose.model('Order', orderSchema);

module.exports = {User, Product, Order, Countries};
