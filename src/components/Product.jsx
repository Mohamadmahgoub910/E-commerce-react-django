import React from 'react'
import { Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

import Rating from './Rating';
function Product({ product }) {
    return (
        <Card className='my-2 rounded'>
            <Link to={`/product/${product._id}`}>
                <Card.Img src={product.image} />
            </Link>
            <Card.Body>
                <Link to={`/product/${product._id}`}>
                </Link>
                <Card.Title as="div">
                    <strong>{product.name}</strong>
                </Card.Title>
            </Card.Body>
            <Card.Text as="div">
                <div className='mx-3'>
                    {/* {product.rating} from {product.numReviews} reviews */}
                    <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                </div>
            </Card.Text>
            <Card.Text className='mx-4' as="h3">
                {product.price}$
            </Card.Text>
        </Card>
    )
}

export default Product
