FROM ubuntu:16.04
MAINTAINER ARO7I <ARO7I@icloud.com>

ARG ID=pwn16
ARG PW=1234
ARG PORT=4416

ENV TZ Asia/Seoul
ENV LC_ALL C.UTF-8
ENV PYTHONIOENCODING UTF-8

COPY zshrc /script/zshrc
COPY vimrc /script/vimrc
COPY gdbinit /script/gdbinit
COPY add_user.sh /script/add_user.sh
COPY start.sh /start.sh

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime &&\
    echo ${TZ} > /etc/timezone &&\
    sed -i "s/archive.ubuntu.com/mirror.kakao.com/g" /etc/apt/sources.list &&\
    dpkg --add-architecture i386 &&\
    apt-get update &&\
    apt-get install curl git wget file zsh sudo vim libssl-dev libffi-dev build-essential netcat-traditional -y &&\
    apt-get install gdb python3 python3-pip python3-dev ruby binutils-multiarch -y &&\
    apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 -y &&\
    apt-get install openssh-server -y &&\
    apt-get upgrade -y &&\
    apt-get autoremove -y &&\
    gem install one_gadget -v 1.7.3 &&\
    useradd -ms /bin/zsh ${ID} &&\
    adduser ${ID} sudo &&\
    adduser ${ID} users &&\
    sed -ri "s/Port 22/Port ${PORT}/g" /etc/ssh/sshd_config &&\
    su - ${ID} sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sed -r 's/exec zsh -l//g') &&\
                      git clone https://github.com/djui/alias-tips.git /home/${ID}/.oh-my-zsh/custom/plugins/alias-tips" &&\
    cp /script/zshrc /home/${ID}/.zshrc &&\
    cp /script/vimrc /home/${ID}/.vimrc &&\
    cp /script/gdbinit /home/${ID}/.gdbinit &&\
    chmod 755 /home/${ID}/.zshrc &&\
    chown ${ID}:users /home/${ID}/.zshrc &&\
    chmod 755 /home/${ID}/.vimrc &&\
    chown ${ID}:users /home/${ID}/.vimrc &&\
    chmod 755 /home/${ID}/.gdbinit &&\
    chown ${ID}:users /home/${ID}/.gdbinit &&\
    chmod 744 /script/add_user.sh &&\
    chmod 750 /start.sh &&\
    su - ${ID} sh -c "pip3 install -U pip==20.3.4 &&\
                      pip3 install -U pwntools &&\
                      git clone https://github.com/longld/peda.git /home/${ID}/.peda &&\
                      sed -ri 's/n\", \"a/ff\", \"a/g' /home/${ID}/.peda/lib/config.py &&\
                      git clone https://github.com/scwuaptx/Pwngdb.git /home/${ID}/.Pwngdb &&\
                      pip3 install -U capstone &&\
                      git clone https://github.com/JonathanSalwan/ROPgadget.git /home/${ID}/.ROPgadget &&\
                      curl -fLo /home/${ID}/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim &&\
                      git clone https://github.com/vim-airline/vim-airline.git /home/${ID}/.vim/plugged/vim-airline &&\
                      git clone https://github.com/vim-airline/vim-airline-themes.git /home/${ID}/.vim/plugged/vim-airline-themes &&\
                      git clone https://github.com/tpope/vim-fugitive.git /home/${ID}/.vim/plugged/vim-fugitive &&\
                      git clone https://github.com/jeetsukumaran/vim-buffergator.git /home/${ID}/.vim/plugged/vim-buffergator &&\
                      git clone https://github.com/preservim/nerdtree.git /home/${ID}/.vim/plugged/nerdtree &&\
                      git clone https://github.com/levelone/tequila-sunrise.vim.git /home/${ID}/.vim/plugged/tequila-sunrise.vim" &&\
    echo "${PW}\n${PW}\n" | passwd root &&\
    echo "${PW}\n${PW}\n" | passwd ${ID}
