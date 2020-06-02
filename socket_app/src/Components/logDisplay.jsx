import React from 'react'
import {connect} from 'react-redux'
import {receiveLog} from '../action/main_action'
import ScrollFeed from 'react-scrollable-feed'

const URL = 'ws://localhost:9000'
const client = new WebSocket(URL)


class LogDisplay extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
        }
    }

    componentDidMount() {

        client.onopen = () => {
            console.log("Websocket Client Connected")
        }

        client.onmessage = (message) => {
            console.log(message)
            this.props.addLog(message.data)
        }

        client.onclose = () => {
            // try to establish the connection again if lost
            this.setState({ws: new WebSocket(URL)})
        }
    }

    componentDidUpdate(){
    }

    render () {
        return (
            <div className="block-dis">
                <h2>Log Tail -f of a file</h2>
                <ScrollFeed forceScroll={true}>
                    {
                        this.props.logs.map((log, i) => {
                            return (
                                <p key={i}>{log}</p>
                            )
                        })
                    }
                </ScrollFeed>
                {/* <div ref={(e1) => {this.logEnd = e1}}></div> */}
            </div>
        )
    }
}

function mapStateToProps(state) {
    return {
        logs: state.logs
    }
}

function mapDispatchToProps(dispatch) {
    return {
        addLog: (log) => {
            dispatch(receiveLog(log))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(LogDisplay)