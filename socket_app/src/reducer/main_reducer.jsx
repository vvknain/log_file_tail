const intialState = {
    logs: []
};

export default function(state = intialState, action) {
    if (action.type === "RECEIVE_LOG") {
        return Object.assign({}, state, {
            logs: state.logs.length == 250 ? state.logs.concat([action.payload]).slice(1) :  state.logs.concat([action.payload])
            // logs: state.logs.concat([action.payload])
        })
    }
    return state
};