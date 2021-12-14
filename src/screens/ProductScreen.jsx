import React, { useState, useEffect } from 'react'
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';
import { Row, Col, Image, ListGroup, Card, Button } from 'react-bootstrap';
import Rating from '../components/Rating';
function ProductScreen({ match }) {
    // Get the id match
    // const product = products.find((p) => p._id === match.params.id)
    const { id } = useParams()
    // const product1 = products.find(el => el._id === id)
    const [product, setProduct] = useState([])
    useEffect(() => {
        async function fetchProduct() {

            const { data } = await axios.get(`/api/products/${id}`)
            setProduct(data)
        }
        fetchProduct()
    }, [])
    return (
        <div>
            <Link to='/' className='btn btn-outline-primary my-3'> Back </Link>
            <Row>
                <Col md={6}>
                    <Image src={product.image} alt={product.name} fluid />
                </Col>
                <Col md={3}>
                    <ListGroup variant='flush'>
                        <ListGroup.Item>
                            <h3> {product.name} </h3>
                        </ListGroup.Item>
                        <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                        <ListGroup.Item>
                            Price: {product.price}$
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Description: {product.description}
                        </ListGroup.Item>
                    </ListGroup>
                </Col>
                <Col md={3}>
                    <Card>
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <Row>
                                    <Col>Price:</Col>
                                    <Col> {product.price} </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Col>Status:</Col>
                                    <Col> {product.countInStock > 0 ? 'inStock' : 'OutStuck'} </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Button className='btn btn-outline-dark mx-3' disabled={product.countInStock === 0} type='button' >Add To Card </Button>
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>
                </Col>
            </Row>


        </div>
    )
}

export default ProductScreen
