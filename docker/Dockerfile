FROM base_node-base

ENV LANG C.UTF-8

ARG project_dir=/usr/src/app/

WORKDIR $project_dir

ARG node_number
ENV node_number=$node_number

ARG node_address
ENV node_address=$node_address

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT "docker/docker-entrypoint.sh" $node_number $node_address
