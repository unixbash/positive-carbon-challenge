import React, {PureComponent} from 'react';
import {AreaChart, Area, Legend, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer} from 'recharts';


export default class CommodityLineChart extends PureComponent {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            data: [],
        };
    }

    getCommodity() {
        fetch("http://localhost:5005/api/coffee")
            .then(result => result.json())
            .then(result => this.setState({data: result}));
    }

    componentDidMount() {
        this.getCommodity();
        this.timer = setInterval(() => this.getCommodity(), 60000);  // Fetch every 60s
    }

    componentWillUnmount() {
        this.timer = null;
    }

    render() {
        return (
            <ResponsiveContainer width="100%" height="100%">
                <AreaChart
                    width={500}
                    height={400}
                    data={this.state.data}
                    margin={{
                        top: 10,
                        right: 30,
                        left: 0,
                        bottom: 0,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3"/>
                    <XAxis dataKey="timestamp"/>
                    <YAxis/>
                    <Tooltip/>
                    <Area type="monotone" dataKey="price" stroke="#8884d8" fill="#8884d8"/>
                </AreaChart>
            </ResponsiveContainer>
        );
    }
}
